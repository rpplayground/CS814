(define (problem problem2)
  (:domain gripper)
  (:objects rooma roomb ball1 ball2 left right)
  (:init (room rooma)
         (room roomb)
         (ball ball1)
         (ball ball2)
	 (gripper left)
	 (gripper right)
         (at-robby rooma)
      	 (free left)
	 (free right)
	 (at ball1 rooma)
	 (at ball2 rooma)
)
  (:goal (and (at ball1 roomb)
  	      (at ball2 roomb)
	 )
  )
)
