---
title: Applet Security
---
# Applet Security
AliceOS has a major focus on privacy and security of user data, especially with the integration of third-party applets. Applets are required to follow the confinement constraints as set by AliceOS's built-in system integrity protection mechanism and with the SEAlice policy, if implemented.

## Security Overview
For those that are familiar with Snapcraft, Applets follow similar sandboxing principles for validation and access:

### Policy 1: Valid Package Identifier

Policy will only permit launch of application from entrypoint if identifier is a proper identifier. Policy will prevent launch of app if identifier is incorrect and would log a application error.

### Policy 2: Strict Arbitrary Execution

Policy will only allow arbitrary access of the host system if manifest declares that it's confinement is `classic`. Apps are isolated by nature and would have no access to sensitive APIs. Block all sensitive API calls if isolated app is not a classic isolation.

## Required manifest data
The following fields are required to comply with these policies:

- `identifier`: the identifier for your Applet. Must follow reverse domain name notation (RDNN).
- `confinement`: the type of confinement your Applet requires.
    - `strict`: The default, sandboxed confinement. Most applets should use this confinement.
    - `classic`: The unsandboxed confinement. Applets that must access the host system natively should use this option instead.