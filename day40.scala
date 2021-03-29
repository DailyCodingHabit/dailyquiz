


import scala.collection.mutable.Set  
val set1: Set[String] = Set("Daily","Coding","Habit")
val set2: Set[String] = Set("Dailly","Coding","Habbit")
val set3 = set1.++(set2)
println(s"${set3 &~ set2}")


