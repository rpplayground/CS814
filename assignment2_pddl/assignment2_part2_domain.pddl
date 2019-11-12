(define (domain transport)

	(:predicates
		(location ?l)
		(package ?p)
		(truck ?t)
		(storage ?s)
		(storage_free ?s)
		(truck_at_location ?t ?l)
		(storage_on_truck ?s ?t)
		(package_in_storage ?p ?s)
		(package_at_location ?p ?l)
		(location_to_location ?l ?l)
	)

	(:action move_truck
	:parameters (?truck ?from ?to)
	:precondition 
	( and
			(location_to_location ?from ?to)
			(truck ?truck)
			(location ?from)
			(location ?to)
			(truck_at_location ?truck ?from)
		)
	:effect
		( and
			(not (truck_at_location ?truck ?from))
			(truck_at_location ?truck ?to)
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