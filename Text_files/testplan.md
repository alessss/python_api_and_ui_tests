CASE1
Placing bet
Priority: Critical
Risk Rationale: This is one of main business features and user flows.
Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<user-id>
    2. Select upcoming football match
    3. Click on desired outcome
    4. Enter valid stake amount
Expected result: bet is placed.

CASE2
Bet API response 200
Priority: Critical
Risk Rationale: This is one of main business features and user flows.
Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<user-id>
    2. Select upcoming football match
    3. Click on desired outcome
    4. Enter valid stake amount
    5. Calculate potential payout as stake * odds, check correct payout is displayed
    6. Place bet
Expected result: response content should correspond endpoint description

CASE3
Stake amount validation positive (parameterized test, to be done via api and automated)
Priority: High
Risk Rationale: Covers one of the validations in main business flow
Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<user-id>
    2. Select upcoming football match
    3. Click on desired outcome
    4. Enter Stake amount and check validation using following params:
        a. 1.01
        b. 50
        c. 100
        d. 1
    5. Place bet
Expected result: Stake amount field allows entering this amount, user can place a bet

CASE4
Stake amount validation negative (parameterized test, to be done via api and automated)
Priority: High
Risk Rationale: Covers one of the validations in main business flow
Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<user-id>
    2. Select upcoming football match
    3. Click on desired outcome
    4. Enter Stake amount and check validation using following params:
        a. -1 -> "-" sign can't be entered
        b. 0 -> Place bet button is deactivated
        c. 1.111 -> entering excess decimals is blocked
        d. 100.01 -> Maximum stake is €100.00 error is displayed
        e. abc -> typing characters is blocked
        f. 001 -> trailing 0 should be cut
Expected result: Stake amount field doesn't allow entering this amount, error message is displayed, 
Place bet button is deactivated

CASE5
Placing bet when balance < Stake amount
Risk Rationale: May cause financial loss if there is a bug
Priority: High
Steps:
    1. Open https://qae-assignment-tau.vercel.app/?user-id=<user-id>
    2. Select upcoming football match
    3. Click on desired outcome
    4. Enter Stake amount > than current user's balance
Expected result: Insufficient balance error is displayed


Much more cases can be added, because the functionality is quite well documented,
but to be in time with the test task, other functionality verification was omitted.

There is a discrepancy in the spec, regarding min stake value.
Business rules say min stake should be 1 EUR, while api validation rules say
mis stake allowed should be 1.01 EUR. In my cases and bugs I assume business
rules of higher priority. This discrepancy requires discussion with BA or stakeholder.

