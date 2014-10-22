#lang racket
(define (bitfunc x) 
  (+ 4 
     (- 
      (expt x 4) 
      (* 5 
         (expt x 2))))) 
(define (bitfunc-rect x1 x2)
  (* (- x2 x1)
     (bitfunc x1)
     ))

(define (bitfunc-recur steps x1 x2)
  (define (step) (/ (- x2 x1) steps))
  
  (if (> steps 0)
             (+ (bitfunc-rect x1 (+ x1 (step))) (bitfunc-recur (- steps 1) (+ (step) x1) x2))
             0))

(define (d x) (exact->inexact x))

(define (bitfunc-iter steps x1 x2)
  (define step 0)
  (set! step (/ (- x2 x1) steps))

  (define area 0)
  (do ((n 0 (+ n 1))) ((>= n steps))
    (set! area (+ area (bitfunc-rect x1 (+ x1 step))))
    (set! x1 (+ x1 step))
    )
  (exact->inexact area))

(define (compare steps x1 x2)
  (abs (- (bitfunc-recur steps x1 x2) (bitfunc-iter steps x1 x2)))
  )

(define (A x y)
         (cond ((= y 0) 0)
               ((= x 0) (* 2 y))
               ((= y 1) 2)
               (else (A (- x 1) (A x (- y 1))))))

(define (gcd a b)
      (if (= b 0)
          a
          (gcd b (remainder a b))))

