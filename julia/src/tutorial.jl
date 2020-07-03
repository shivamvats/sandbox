using Printf
using Statistics

printing = false
casting = false
strings = false
boolean = false
while_loop = false
for_loop = false
arrays = true

if printing
    s = 0
    s = "Dog"
    # println(s)

    function changeNum()
        x::Int8 = 10
        x = "Dog"
    end

    changeNum()
end

# Casting
if casting
    c2 = Char(120)
    println(c2)

    f1 = parse(Float64, "1")
    println(f1)

    i1 = parse(Int8, '1')
    println(i1)
end

if strings
    s1 = "some random string"
    println("Length: ",  length(s1))
    println("Index 1: ", s1[1])
    println("Last: ", s1[end])
    println("Slice: ", s1[1:4])

    s2 = string("Shivam", "Vats")
    println(s2)
    println("Shivam" * "Vats")
    i1 = 5
    i2 = 8
    println("$i1 + $i2 = $(i1 + i2)")
end

if boolean
    name = "Shivam"
    age = 25
    if name == "Shivam" && age == 25
        println("You are awesome")
    end
end

if while_loop
    i = 1
    while i < 20
        if(i % 2) == 0
            println(i)
            global i += 1
            continue
        end
        global i += 1
        if i >= 10
            break
        end
    end
end

if for_loop
    for i = 1:5
        println(i)
    end
    for i in [2, 4, 5]
        println(i)
    end
    # Double loop
    for i = 1:5, j = 2:2:10
        println((i, j))
    end
end

if arrays
    a1 = zeros(Int32, 2, 2)
    a2 = Array{Int32}(undef, 5)
    a3 = Float64[]
    a4 = [1, 2, 3, 4]
    println("Array: ", a4)
    println("First: ", a4[1])
    println("Last: ", a4[end])
    println(3 in a4)

    f(a) = (a >= 2) ? true : false
    println("findall")
    println(findall(f, a4))
    println("count")
    println(count(f, a4))

    a5 = [[1,2]; [3,4]]
    println("Array: ", a5)
    println("size: ", size(a5))
    println("length: ", length(a5))
    println("sum: ", sum(a5))

    println("Numpy like")
    println(a5 * 2)
    println(maximum(a5))
    println(minimum(a5))

    println("splicing ", a5)
    splice!(a5, 2, 9)
    println(a5)
    splice!(a5, 1:2, 8:9)
    println(a5)
    splice!(a5, 2:1, 6:7)
    println(a5)

    a6 = [1, 'c', "shivam"]
    println("non-uniform arrays: ", a6)
    a7 = [sin, cos, tan]
    println("Store functions in arrays: ", a7)
    for n in a7
        println(n(0))
    end

    println("\nMulti dim arays")
    a8 = [1 2 3; 4 5 6]
    println(a8)
    print("Looping")
    for n = 1:2, m = 1:3
        println(a8[n, m])
    end

    println("collect converts ranges into vectors")
    a9 = collect(1:5)
    println(1:5, " ", a9)
    println(2:2:10, " ", collect(2:2:10))
end

