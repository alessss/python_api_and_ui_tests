Why you selected these 2 tests for automation over other candidates?

I selected these 2 tests, because they cover main business functionality
both from API level and UI level and guarantee that core functionality works.

What you intentionally left as manual only and why?

Of course a lot more tests should be automated, including UI. But we always
should keep balance between number of automated UI tests and time to support
these automated tests.

Your top 2–3 recommendations if this project were to scale (CI/CD, additional test layers, data
strategy, spec clarifications, etc)?

- Clarify min stake amount requirement
- Cover each endpoint with 200 (201), 400, 422 status, parameterize API tests
- Create CI/CD pipeline to be able to run tests and get reports at test management system (eg TestRail)
- Connect AI agent for code review of tests (Copilot)
- Think of test review process for tests