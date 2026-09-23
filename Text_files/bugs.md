Bug-1
Past matches are displayed on Match list
Severity: High
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Check date of the top match
Expected result: Only upcoming football matches should be displayed (requirement 2.1) 
Actual result: Past football matches are displayed
Business Impact: it takes time for user to understand that matches displayed 
have already passed and it also takes time to filter the result. Negative impact
on user experience.
Evidence: Screenshots/screenshot_1.png

Bug-2
User can place a bet on passed match
Severity: Critical
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Find passed match (use date filters if needed)
    3. Click on desired outcome
    4. Enter valid stake amount
    5. Click Place bet button
    6. Close Bet placed succesfully modal window
    7. Update the page
Expected result: User shouldn't be able to place bet on passed match
Actual result:
    1. User can place bet on passed match
    2. User's balance is decreased after placing bet on passed match
Business Impact: critical flow is broken. 
Evidence: Screenshots/screenshot_2.png

Bug-3
Wrong potential payout on Success place bet displayed on modal window
Severity: Critical
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Place valid bet (future match and valid amount)
    3. Wait, until success modal window is displayed
Expected result: Potential payout should be calculated as odds*stake
Actual result: Potential payout on Success modal window always equals stake * 2
API returns correct amount.
Business Impact: wrong data during critical flow is displayed for user. 
Evidence: Screenshots/screenshot_3.png

Bug-4
Wrong currency in place-bet response
Severity: Critical
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Place valid bet (future match and valid amount)
    3. Check place-bet response
Expected result: according to response description currency should be EUR
Actual result: currency is USD
Business Impact: may have major influence on finance, requires further investigation.
If wrong bet currency inserted into database, may lead to potential finance losses.
Evidence: Screenshots/screenshot_3.png

Bug-5
Trailing 0 can be entered in Stake field
Severity: Low
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Select match and desired outcome
    3. Type 001 as Stake amount
Expected result: trailing 0 shouldn't be allowed, because min stake amount is 1
Actual result: trailing zeros are allowed (later they are cut on client side before sending the request)
Business Impact: No. Minor cosmetic issue

Bug-5
Stake field is not limited by length
Severity: Low
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Select match and desired outcome
    3. Type 1000000000000000 as Stake amount
Expected result: max 6 characters should be allowed, because max stake amount is 100.00
Actual result: field has no limit in characters
Business Impact: No. Minor cosmetic issue

Bug-6
Odds range filter values can be vice versa
Severity: Medium
Reproduction Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<candidate_id>
    2. Click Odds filter
    3. Enter MIN > MAX manually
    4. Enter MIN > MAX manually by moving dot
Expected result: Entering MIN > MAX shouldn't be allowed by both methods
Actual result: Entering MIN > MAX is not blocked by both metods
Business Impact: No business impact, bad user experience.
Evidence: Screenshots/screenshot_4.png

Much more bugs can be found,
but to be in time with the test task, other functionality verification was omitted.

Low priority issues intentionally included into the report, to show my skills in setting correct priority for bugs. 
There are still bugs of higher priority not described in this document. 


