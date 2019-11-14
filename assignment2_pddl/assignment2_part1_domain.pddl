(define (domain transport)

	(:predicates
		(location ?l)
		(package ?p)
		(truck ?t)
		(truck_at_location ?t ?l)
		(package_at_location ?p ?l)
		(package_on_truck ?p ?t)
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
	:parameters (?package ?location ?truck)
	:precondition
		( and
			(package ?package)
			(location ?location)
			(truck ?truck)
			(truck_at_location ?truck ?location)
			(package_at_location ?package ?location)
		)
	:effect
		(and
			(not (package_at_location ?package ?location))
			(package_on_truck ?package ?truck)
		)
	)

	(:action drop_off
	:parameters  (?package ?location ?truck)
	:precondition
		(and
			(package ?package)
			(location ?location)
			(truck ?truck)
			(package_on_truck ?package ?truck)
			(truck_at_location ?truck ?location)
		)
	:effect
		(and
			(not (package_on_truck ?package ?truck))
			(package_at_location ?package ?location)
		)	
	)
)