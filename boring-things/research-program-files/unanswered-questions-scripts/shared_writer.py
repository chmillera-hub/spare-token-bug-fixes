# One connection per device, one reader task per device, and a queue that lets any function send to a device
# (Python forum topic 93342). Two small local servers stand in for the two Telnet devices.
import asyncio, re, sys
print("Python", sys.version.split()[0])
rules = [("~DEVICE,PadOffice,9,3", "*1,23,1"), ("~DEVICE,PadOffice,7,.", "*1,24,0")]
received_by_tuner = []; connections = {"lutron": 0, "tuner": 0}

async def lutron_server(reader, writer):
    connections["lutron"] += 1
    for line in ("~DEVICE,PadOffice,9,3", "~OUTPUT,5,1,100.00", "~DEVICE,PadOffice,7,4"):
        writer.write((line + "\r\n").encode()); await writer.drain(); await asyncio.sleep(0.05)
    await asyncio.sleep(0.3); writer.close()
async def tuner_server(reader, writer):
    connections["tuner"] += 1
    while line := await reader.readline(): received_by_tuner.append(line.decode().strip())

class Device:
    # owns the single connection to one device; everything that wants to send puts text into the queue
    def __init__(self, name): self.name = name; self.outbox = asyncio.Queue()
    async def connect(self, host, port):
        self.reader, self.writer = await asyncio.open_connection(host, port)   # telnetlib3.open_connection returns the same kind of pair
        self.sender = asyncio.create_task(self._send_loop())
    async def _send_loop(self):
        while True:
            text = await self.outbox.get()
            self.writer.write((text + "\r\n").encode()); await self.writer.drain()   # only this task ever touches the writer
            self.outbox.task_done()
    def send(self, text): self.outbox.put_nowait(text)                        # safe to call from any function

async def watch_lutron(lutron, tuner):
    while line := await lutron.reader.readline():
        text = line.decode().strip()
        for pattern, action in rules:
            if re.fullmatch(pattern, text): tuner.send(action)
async def heartbeat(tuner):
    for i in range(3):
        tuner.send(f"?PING,{i}"); await asyncio.sleep(0.06)

async def main():
    s1 = await asyncio.start_server(lutron_server, "127.0.0.1", 0); s2 = await asyncio.start_server(tuner_server, "127.0.0.1", 0)
    lutron, tuner = Device("lutron"), Device("tuner")
    await lutron.connect("127.0.0.1", s1.sockets[0].getsockname()[1]); await tuner.connect("127.0.0.1", s2.sockets[0].getsockname()[1])
    await asyncio.gather(watch_lutron(lutron, tuner), heartbeat(tuner))       # two different functions send to the same device
    await tuner.outbox.join(); await asyncio.sleep(0.1)
    print("connections opened per device:", connections)
    print("lines that reached the tuner:", received_by_tuner)
    print("both rule actions arrived:", {"*1,23,1", "*1,24,0"} <= set(received_by_tuner), "| all three heartbeat lines arrived:", sum(l.startswith("?PING") for l in received_by_tuner) == 3, "| every line arrived whole:", all(re.fullmatch(r"(\*1,2[34],[01])|(\?PING,\d)", l) for l in received_by_tuner))
asyncio.run(main())
