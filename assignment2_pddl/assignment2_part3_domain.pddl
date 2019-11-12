(define (domain transport)

	(:predicates
		(location ?l)
		(package ?p)
		(truck ?t)
		(storage ?s)
		(canister ?c)
		(storage_free ?s)
		(truck_at_location ?t ?l)
		(storage_on_truck ?s ?t)
		(package_in_storage ?p ?s)
		(package_at_location ?p ?l)
		(location_to_location ?l ?l)
		(canister_at_location ?c ?l)
		(canister_on_truck ?c ?t)
		(canister_used ?c)
	)

	(:action move_truck
	:parameters (?truck ?from ?to ?c)
	:precondition 
	( and
			(location_to_location ?from ?to)
			(truck ?truck)
			(location ?from)
			(location ?to)
			(canister ?c)
			(canister_on_truck ?c ?truck)
			(truck_at_location ?truck ?from)
		)
	:effect
		( and
			(not (truck_at_location ?truck ?from))
			(truck_at_location ?truck ?to)
			(not (canister_on_truck ?c ?truck))
			(canister_used ?c)
		)
	)

	(:action refuel_truck
	:parameters (?truck ?l ?c)
	:precondition 
	( and
			(truck ?truck)
			(location ?l)
			(canister ?c)
			(canister_at_location ?c ?l)
			(truck_at_location ?truck ?l)
		)
	:effect
		( and
			(not (canister_at_location ?c ?l))
			(canister_on_truck ?c ?truck)
		)
	)

	(:action pick_up
	:parameters (?package ?location ?truck ?storage)
	:precondition
		( and
			(package ?package)
			(location ?location)
			(truck ?truck)
			(storage ?storage)
			(storage_on_truck ?storage ?truck)
			(storage_free ?storage)
			(truck_at_location ?truck ?location)
			(package_at_location ?package ?location)
		)
	:effect
		(and
			(not (package_at_location ?package ?location))
			(not (storage_free ?storage))
			(package_in_storage ?package ?storage)
		)
	)

	(:action drop_off
	:parameters  (?package ?location ?truck ?storage)
	:precondition
		(and
			(package ?package)
			(location ?location)
			(truck ?truck)
			(storage ?storage)
			(storage_on_truck ?storage ?truck)
			(package_in_storage ?package ?storage)
			(truck_at_location ?truck ?location)
		)
	:effect
		(and
			(not (package_in_storage ?package ?storage))
			(storage_free ?storage)
			(package_at_location ?package ?location)
		)	
	)
)