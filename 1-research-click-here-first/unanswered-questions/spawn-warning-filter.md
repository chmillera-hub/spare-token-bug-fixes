# Silencing an import warning inside a spawned Python child process

## Link to the original question

https://discuss.python.org/t/105472

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 on Python 3.13.18 and no other person has rerun the tests yet which means the page is unconfirmed.

## The question

On 31 December 2025 somebody asked on the Python help forum how to set a warning filter in a child process before the child imports a module that prints a UserWarning on import.
The asker starts child processes with the Process class of a spawn context and that class has no setup hook that runs before imports.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

The tests used a small module that raises a UserWarning on import and a child started with the spawn method.

- With the noisy import at the top of the child file and no other change the child printed the warning even though the parent had a filter because a spawned child starts as a fresh Python with default filters.
- Route 1 worked: setting os.environ["PYTHONWARNINGS"] = "ignore::UserWarning" in the parent before starting the child silenced the warning because the child inherits the environment and Python reads that variable at startup.
- Route 2 worked: calling warnings.filterwarnings inside the target function and importing the noisy module on the next line (inside the function) silenced the warning.
- Route 3 worked: a tiny module whose only content is the filterwarnings call silenced the warning when the child file imports the tiny module before the noisy module.

## Best-guess answer

Route 1 needs one line in the parent and no change to the child code and the filter text can be narrowed to one module (for example "ignore::UserWarning:noisy_module").
Route 2 and route 3 keep the fix inside the code and affect only the files that use them.
All three routes returned the correct result (42) from the child in the tests.

The test files sit in boring-things inside research-program-files inside unanswered-questions-scripts inside a folder named spawn-warning-test.
