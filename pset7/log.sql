-- Keep a log of any SQL queries you execute as you solve the mystery.
-- we have to solve the mistery of Theft of CS50 DUCK
-- we have to start with the screening of crime reports for the day
SELECT * FROM crime_scene_reports WHERE day = 28 and month = 7 and street = "Chamberlin Street";
-- 2020 | 7 | 28 | Chamberlin Street | Theft of the CS50 duck took place at 10:15am at the chamberlin street courthouse
-- Interviews were conducted today with three withnesses who were present at the time _ each  of their interview transcripts mentions the courthouse.

-- Lets start with the remarks from the interviews 
-- The word courthouse is used in the remarks of reporters
SELECT * FROM interviews WHERE day = 28 and month = 7 and year = 2020 and transcript LIKE "%Courthouse%"











SELECT * FROM courthouse_security_logs WHERE day = 28 and month = 7 and year = 2020 and hour = 10 and minute BETWEEN 15 and 25;















SELECT * FROM people WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '322W7JE');












SELECT * FROM flights JOIN airports ON airports.id = flights.origin_airport_id WHERE day = 29 and month = 7 and year = 2020 and city = "Fiftyville";













SELECT * FROM passengers JOIN flights ON passengers.flight_id = flights.id WHERE origin_airport_id = 8 and day = 29 and month = 7 and year = 2020 and hour = 8 and minute = 20 
and passport_number IN ('2963008352', '7526138472', '7049073643', '1695452385', '8496433585', '3592750733', '5773159633');









SELECT * FROM people WHERE passport_number IN ('1695452385', '5773159633', '8496433585');











SELECT * FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE person_id IN ('398010', '467400', '686048');








SELECT * FROM atm_transactions WHERE day = 28 and month = 7 and year = 2020 and atm_location = "Fifer Street" and account_number IN (28500762, 49610011);










SELECT * FROM phone_calls WHERE day = 28 and month = 7 and year = 2020 and caller IN ('(367) 555-5533', '(389) 555-5198') and duration <= 60;











SELECT * FROM flights JOIN airports ON airports.id = flights.destination_airport_id JOIN passengers ON passengers.flight_id = flights.id
WHERE day = 28 and month = 7 and year = 2020 and passport_number = 5773159633;









SELECT * FROM phone_calls WHERE day = 28 and month = 7 and year = 2020 and caller = '(367) 555-5533' and duration <= 60;






SELECT * FROM people WHERE phone_number = '(375) 555-8161';
