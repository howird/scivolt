Distrubteed Ambedded PAlications
eg. earospace autmotives, defence

- comprised of distrubuted nodes (ECU-electronic control units)
- need off -schip network
- puts cumputing power near the event
	- shorter delays for sensing/actuation
	- communicate processed data not raw data
- mixed criticality
	- eg aircraft
		- control network: safety critical, dedicated h/w protocols
		- management: missision critical (eg navigation)
		- passage network: internet connected, open protocol

# canbus contorller area network

- introduced by bosch in 1985, and has now become fairly widespread
- orignal specification had max speed of 1mbps
- mandated for on board auto, diagnostics in NA and EUR
- serial - twisted pair differential signalling
	- boadcast, any node can send, anything connected to bus can see the broad cast

diagram

- open drain is a wired or and this is a wired and

- theres no addresses on the bus, only message ids, each node will have its own message id
- the message id has 1 sender and 1+ eceivers
- the message id defines the message priority via wired-and
- arbitration
	- wait for idle bus
	- start sending its msg ID and will drop out if it senses a dominant (0) while transmitting a recessive (1)

diagram

- lower messaged IDs have higher priority,
- in practice msbiits can be used for priority and lsbits to identirfy a recipient

- 4 frame types
	- data - ECU output data
	- remote - request for ECU daa
	- error
	- overload - flow control

diagram

- nodes sync their clocks to SoF (start of frame)
- uses bit staffing to maintain synchronization during fram transmission: after 5 bits of like polarity a bit of apposing polarity is inserted
- CAN FD has up to 64B data frames

## FlexRay

- a replacement for flexray
- 