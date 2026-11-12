# Letting several async functions send to one device over a single connection

## Link to the original question

https://discuss.python.org/t/93342

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 with two small local servers standing in for the two Telnet devices and plain asyncio connections standing in for telnetlib3 and no other person has rerun the test yet which means the page is unconfirmed. Real devices and the telnetlib3 library itself were not tested.

## The question

On 26 May 2025 somebody new to Python asked on the Python help forum about a home automation program that listens to one device and sends commands to another device over Telnet.
Each device allows only four connections so the asker wants exactly one connection per device with one reading function per device and wanted to know how several async functions can share one outgoing writer and whether the design is workable.
The post had zero replies when the forum list was read on 12 November 2026.

## The design that was tested

Each device gets one small object that owns the single connection.
The object has an outbox (an asyncio.Queue) and one background task that takes text from the outbox and writes the text to the device.
Any function that wants to send calls device.send(text) which only puts the text into the outbox.
Because only the one background task ever touches the writer two functions can never write at the same moment.

## What the test shows

- Exactly 1 connection was opened per device.
- Two different functions sent to the same device (a rule matcher reacting to lines from the first device and a separate heartbeat function).
- All five lines reached the second device: both rule actions and all three heartbeat lines.
- Every line arrived whole with no mixing of two messages.

## Best-guess answer

The design in the question is workable and the outbox queue is the piece that makes sharing safe.
The core of the tested class:

class Device:
    def __init__(self): self.outbox = asyncio.Queue()
    async def connect(self, host, port):
        self.reader, self.writer = await telnetlib3.open_connection(host, port)
        self.sender = asyncio.create_task(self._send_loop())
    async def _send_loop(self):
        while True:
            text = await self.outbox.get()
            self.writer.write(text + "\r\n")
            await self.writer.drain()
    def send(self, text): self.outbox.put_nowait(text)

One line in the posted program looks wrong: tuner_writer.writelines(action, "\n") passes two arguments and writelines expects one list of lines so writer.write(action + "\r\n") is the form worth using. The telnetlib3 behaviour of that line was not tested.

The test file named shared_writer.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
