len :: [Char] -> Int
len [] = 0
len (x:xs) = 1 + len xs

devolverListaSnd :: [(Char, Char)] -> [Char] -> [Char]
devolverListaSnd l [] = []
devolverListaSnd l (x:xs) | len(x:xs) >= 1 = iEsimoSegundoelemento index l : devolverListaSnd l xs
                          | otherwise = []
                          where index = buscarEnPrimeroselementos x l

iEsimoSegundoelemento :: Int -> [(Char, Char)] -> Char
iEsimoSegundoelemento i l = buscarDesde i l 0

buscarDesde :: Int -> [(Char, Char)] -> Int -> Char
buscarDesde i (x:xs) n | i == n = snd x
                       | otherwise = buscarDesde i xs (n+1)

buscarEnPrimeroselementos :: Char -> [(Char, Char)] -> Int
buscarEnPrimeroselementos c l = buscarDesdePrimeroselementos c l 0

buscarDesdePrimeroselementos :: Char -> [(Char, Char)] -> Int -> Int
buscarDesdePrimeroselementos c [] n = n
buscarDesdePrimeroselementos c (x:xs) n | c == fst x = n
                                        | otherwise = buscarDesdePrimeroselementos c xs (n+1)