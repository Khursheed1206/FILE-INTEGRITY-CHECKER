# FILE-INTEGRITY-CHECKER

*COMPANY*:CODTECH IT SOLUTIONS

*NAME*: KHURSHEED JAHAN

*INTERN ID*: CT04DF2054

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

##DESCRIPTION OF TASK1- FILE-INTEGRITY-CHECKER##

Description:
The File Integrity Checker is a Python-based utility designed to monitor a designated folder and detect any changes made to its contents. It actively checks for file creations, deletions, and modifications by computing and comparing cryptographic hashes. This enables the user to ensure that no unauthorized or unexpected changes have occurred. It operates by taking a snapshot of all the files within the monitored folder, generating their hash values using SHA-256, and regularly rechecking them to detect any discrepancies. If a file is modified, added, or removed, the application outputs a message indicating the change and the time it occurred.
The primary motivation behind this tool is file integrity and security. In environments where data security and auditability are critical—such as corporate, academic, and personal computing contexts—being aware of even the smallest file-level change can be vital. Whether for compliance with industry regulations or for peace of mind, this tool ensures users can track changes in real time or over a defined interval.


Core Functionality
-> Continuously monitors a specified folder for:

   1.New files being added.

   2.Existing files being deleted.

   3.Files being altered (content-level modification).

-> Hash comparison is used to identify exact file changes.

-> Terminal output provides live updates of file integrity status.


Platform & Tools Used:

Platform:
The File Integrity Checker is a Python-based utility designed to monitor a designated folder and detect any changes made to its contents. It actively checks for file creations, deletions, and modifications by computing and comparing cryptographic hashes. This enables the user to ensure that no unauthorized or unexpected changes have occurred. It operates by taking a snapshot of all the files within the monitored folder, generating their hash values using SHA-256, and regularly rechecking them to detect any discrepancies. If a file is modified, added, or removed, the application outputs a message indicating the change and the time it occurred.
The primary motivation behind this tool is file integrity and security. In environments where data security and auditability are critical—such as corporate, academic, and personal computing contexts—being aware of even the smallest file-level change can be vital. Whether for compliance with industry regulations or for peace of mind, this tool ensures users can track changes in real time or over a defined interval.


Programming Language:
The File Integrity Checker is a Python-based utility designed to monitor a designated folder and detect any changes made to its contents. It actively checks for file creations, deletions, and modifications by computing and comparing cryptographic hashes. This enables the user to ensure that no unauthorized or unexpected changes have occurred. It operates by taking a snapshot of all the files within the monitored folder, generating their hash values using SHA-256, and regularly rechecking them to detect any discrepancies. If a file is modified, added, or removed, the application outputs a message indicating the change and the time it occurred.
The primary motivation behind this tool is file integrity and security. In environments where data security and auditability are critical—such as corporate, academic, and personal computing contexts—being aware of even the smallest file-level change can be vital. Whether for compliance with industry regulations or for peace of mind, this tool ensures users can track changes in real time or over a defined interval.


Development Environment:
A dedicated virtual environment (.venv) was created within the PyCharm project to isolate dependencies and ensure compatibility without affecting system-wide Python installations.


Tools & Libraries Used:
os: Enables access to the operating system’s file paths and directories.

hashlib: Used to generate secure hashes (SHA-256) for verifying file contents.

time: Facilitates periodic scanning by introducing timed delays in the loop.


Applications:
1.Security & Compliance: Detect unauthorized changes in system or config files.

2.Academic & Research: Ensure raw data files remain untouched throughout experiments.

3.Corporate: Monitor shared folders for accidental or malicious changes.

4.Backup Validation: Track changes and confirm the integrity of backup files.



