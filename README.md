# two-time-pad-attack

This Python script demonstrates how to bypass an one-time password encryption when the password has been reused.

If the attacker has access to two (or more) ciphertexts encyrpted with the same key it's possible to guess words present in one of the plaintexts and (partially) decrypt the other ciphertexts.

Resources I used to understand how the attack works:

- https://crypto.stackexchange.com/questions/2249/how-does-one-attack-a-two-time-pad-i-e-one-time-pad-with-key-reuse
- http://www.crypto-it.net/eng/attacks/two-time-pad.html
