# Why datetime.strptime with %Z returns a time without a time zone

## Link to the original question

https://discuss.python.org/t/86433

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 on a machine set to US Central time and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 29 March 2025 somebody asked on the Python help forum why datetime.strptime("2025-UTC", "%Y-%Z") returns a datetime without time zone information while "%z" with "+0000" returns a time-zone-aware datetime.
The asker saw the same behaviour from Python 3.5 to 3.13 and asked whether the behaviour is intended and what %Z is for.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- %Z with "UTC" returned a datetime with tzinfo None and %z with "+0000" returned a datetime with tzinfo UTC which matches the report.
- %Z accepted only a short list of names on the test machine: UTC and GMT and CST (a local zone name of the machine). The names EST and CET and Europe/Paris were refused with an error.
- Using %Z and %z together gave an aware datetime whose zone name is the text matched by %Z.

## Best-guess answer

The behaviour fits the design as far as the tests show: a zone name such as CST does not pin down an offset from UTC (the same letters are used for more than one zone in the world) so %Z only checks that the text is a known name and keeps the name for labeling when %z supplies the offset.
The consistency across many Python versions points to intended behaviour and the page did not find a statement from the Python developers saying so.
Two routes to an aware result worked in the tests:

- When the text is known to say UTC: datetime.strptime(text, "%Y-%m-%d %H:%M %Z").replace(tzinfo=datetime.timezone.utc)
- When the text ends in a zone name such as Europe/Paris: split the name off and attach zoneinfo.ZoneInfo(name) after parsing the rest.

The test file named strptime_zone.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
