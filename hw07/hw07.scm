(define (add-leaf t x)
  (if (is-leaf t)
      t
      (begin (define mapped-branches
                     (map  (lambda (t) (add-leaf t x)) (branches t)))
             (tree (label t)
                   (append mapped-branches (list (tree x nil)))))))
