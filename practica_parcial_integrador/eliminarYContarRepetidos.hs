eliminarYContarRepetidos :: [Int] -> ([Int], [(Int, Int)])
eliminarYContarRepetidos l = (elemRep l, contarElemRep l (elemRep l))

contarElemRep :: [Int] -> [Int] -> [(Int, Int)]
contarElemRep l [] = []
contarElemRep l (x:xs) | apariciones x l < 2 = contarElemRep l xs
                       | otherwise = (x, (apariciones x l) - 1) : contarElemRep l xs


elemRep :: [Int] -> [Int]
elemRep [] = []
elemRep (x:xs) | apariciones x xs >= 1 = x : elemRep (sacarElemDe x xs)
               | otherwise = x : elemRep xs



sacarElemDe :: Int -> [Int] -> [Int]
sacarElemDe _ [] = []
sacarElemDe elem (x:xs) | x == elem = sacarElemDe elem xs
                        | otherwise = x : sacarElemDe elem xs


apariciones :: Int -> [Int] -> Int
apariciones _ [] = 0
apariciones elem (x:xs) | x == elem = 1 + apariciones elem xs
                        | otherwise = apariciones elem xs


pertenece :: Int -> [Int] -> Bool
pertenece _ [] = False
pertenece elem (x:xs) = (x == elem) || pertenece elem xs


longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
