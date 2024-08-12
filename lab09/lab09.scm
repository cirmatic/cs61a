(define (over-or-under num1 num2) 
        (cond ((< num1 num2) -1)
              ((= num1 num2) 0)
              ((> num1 num2) 1)))
              

(define (make-adder num) 
        (define (re_prosedure inc)
                (+ num inc))
        re_prosedure
        )

(define (composed f g) 
        (lambda (x) (f (g x)))) 

(define (repeat f n) 
        (define (repeat_n x)
                (define (repeat__n x n) 
                (if (zero? n) x (repeat__n (f x) (- n 1))))
                (repeat__n x n))
        repeat_n) 

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
        (define c (max a b))
        (define d (min a b))
        (if (zero? (modulo c d)) d (gcd d (modulo c d)))) 


(define (duplicate lst) 
        (if (null? lst) nil (cons (car lst) (cons (car lst) (duplicate(cdr lst))))))

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
        (if (null? s) nil
        (if (list? (car s)) (cons (deep-map fn (car s))
                             (deep-map fn (cdr s)))
                           (cons (fn (car s))
                            (deep-map fn (cdr s))))))
