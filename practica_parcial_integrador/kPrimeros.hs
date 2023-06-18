type Nombre = [Char]

kPrimeros :: [(Nombre, Int)] -> Int -> [Nombre]

kPrimeros l k | k > 0 = (fst maximo) : kPrimeros (quitarElem maximo l) (k-1)
              | otherwise = []
              where maximo = obtenerMax l
            
obtenerMax :: [(Nombre, Int)] -> (Nombre, Int)
obtenerMax (x:xs) = maxComparador x xs

maxComparador :: (Nombre, Int) -> [(Nombre, Int)] -> (Nombre, Int)
maxComparador m [] = m
maxComparador m (x:xs) | snd x > snd m = maxComparador x xs
                       | otherwise = maxComparador m xs 

quitarElem ::(Nombre, Int) -> [(Nombre, Int)] -> [(Nombre, Int)]
quitarElem _ [] = []
quitarElem elem (x:xs) | x == elem = quitarElem elem xs
                       | otherwise = x : quitarElem elem xs
