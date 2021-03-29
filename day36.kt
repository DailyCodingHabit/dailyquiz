

package org.kotlinlang.play

fun addNumbers(n1: Double, n2: Double, n3: Double): Int {
    val sum = n1 + n2 * n3.toInt()
    val sumInteger = sum.toInt()
    return sumInteger
}

fun main() {
    val number1 = 2.2
    val number2 = 1.2
    val result: Int

    result = addNumbers(number1, number2, 2.5)
    println("$result")
}




// 4