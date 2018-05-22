# SIP based VoIP Calls

**Session Initiation Protocol (SIP)**, a client-server protocol is used in this project. SIP is used to establish the session between two parties or more. It is a communication protocol, used for call signaling and controlling multimedia sessions in application for Voice, Video and messaging over IP networks.

It is an application as well as Session Layer Protocol, depending on the functionality it performs at an instance. It work in corporation with other application layer protocols such as H.323. 

In my project, I have used 4 machines, out of which one is one is working as a Server, while rest three are clients. The machine running as Server has a Linux OS; while clients are operated on Windows OS.

I have considered **four** call conditions, which includes - 

1. **Call Establishment** - Call is established between client and server with different IDs.

2. **Busy User** - In this mode of operation, one user tries to call other user, but the other user is busy. The time duration for which user wants to set the busy mode is sent as an argument in the extension.conf file.

3. **Call On Hold** - In this phase, a third user calls first user with ID 100, which is already in call with second user. He then keeps the call on HOLD and establishes the call with the third user.

4. **Call Conferencing** - In this scenario, 3rd user calls 1st one, while a call is already in process within 1st and 2nd user. The second user puts on Hold and establishes the call and then again invites first user and a conferencing call is established.

In the 2nd part of project, I developed a **Python Script** and used PJSIP library for the implementation of SIP.

Also, I have calculated MoS Value of the calls between the users, by pinging them and watching the successful packet delivery from one user to the other. Although the MoS Value came out to be great (maximum) since the calls were made on a LAN connection.

