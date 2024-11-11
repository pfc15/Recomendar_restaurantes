
-- Main function to run the program
main :: IO ()
main = do
    let restaurantes = [("subway",7,25),("espoleto",9,30),("ru",6,7),("frangrão_pf",8,27),("marmita",4,15),("grego",8,22),("natural",7,22),("frangrão_hamburguer",7,22)]
    print (knapsack restaurantes 200 0 1)

knapsack::[(String,Int, Int)]-> Int -> Int -> Int-> (Int,[String])
knapsack [] _  _ _ = (0, [])
knapsack _ 0 _ _ = (0, [])
knapsack lista orcamento felicidade repeticoes
    | itemCost > orcamento = knapsack (init lista) orcamento felicidade 1
    | otherwise = 
        let (totalWithItem, itemsWithItem) = knapsack lista (orcamento - itemCost) (felicidade + itemHappiness `div` repeticoes) (repeticoes + 1)
            withItemResult = (totalWithItem + itemHappiness `div` repeticoes, itemName : itemsWithItem)

            (totalWithoutItem, itemsWithoutItem) = knapsack (init lista) orcamento felicidade 1
        in if fst withItemResult > totalWithoutItem
           then withItemResult
           else (totalWithoutItem, itemsWithoutItem)
  where
    (itemName, itemHappiness, itemCost) = last lista