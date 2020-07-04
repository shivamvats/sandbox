using Printf
using Statistics

printing = false
casting = false
strings = false
boolean = false
while_loop = false
for_loop = false
arrays = false
random = false
tuple = false
dict = false
fn1 = false
fn2 = false
fn3 = false
anon_fn = false
symbols = false
julia_struct = false
abstract_types = false
files = true

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

if random
    A = rand(-10:10, 5, 5)
    println("Random Matrix ", A)

    for r = 1:5
        for c = 1:5
            print(A[r, c], " ")
        end
        print("\n")
    end
end

if tuple
    t1 = (1, 2, 3, 4)
    println(t1)
    for i in t1
        println(i)
    end

    name_age = (shivam = ("Shivam", 25), ram = ("Ram", 27))
    println(name_age.shivam)
end

if dict
    d1 = Dict("pi" => 3.14, "e" => 2.718)
    println(d1["pi"])
    d1["golden"] = 1.618
    println(d1)
    println(haskey(d1, "pi"))
    delete!(d1, "pi")
    println(haskey(d1, "pi"))

    for kv in d1
        println(kv)
    end

    for (key, value) in d1
        println(key, ":", value)
    end
end

if fn1
    getSum(x, y) = x + y
    x, y = 1, 2
    @printf("%d + %d = %d\n", x, y, getSum(x, y))

    function canIVote(age=16)
        if age > 18
            println("You can vote")
        else
            println("You can't vote")
        end
    end
    canIVote(25)

    v1 = 5
    function changeV1()
        global v1 = 8
    end
    changeV1()
    println(v1)
end

if fn2
    function getSum2(args...)
        sum = 0
        for a in args
            sum += a
        end
        println(sum)
    end
    getSum2(1, 2, 3, 4)

    function next2(val)
        return (val + 1, val + 2)
    end
    println(next2(5))

    # Return a function
    function makeMultiplier(num)
        return function(x) return x * num end
    end
    mult3 = makeMultiplier(3)
    println(mult3(6))
end

if fn3
    function getSum3(num1::Number, num2::Number)
        return num1 + num2
    end

    function getSum3(num1::String, num2::String)
        return parse(Int32, num1) + parse(Int32, num2)
    end

    println("3 + 4 = ", getSum3(3, 4))
    println("3 + 4 = ", getSum3("3", "4"))
end

if anon_fn
    v1 = map(x -> x * x, [1, 2, 3])
    println(v1)

    v2 = map((x, y) -> x*y, (1, 2), (4, 4))
    println(v2)

    v3 = reduce(+, 1:100)
    println(v3)

    sentence = "This is a string"
    sArray = split(sentence)
    longest = reduce((x, y) -> length(x) > length(y) ? x : y, sArray)
    println("Longest word in ", sentence, " is ", longest)
end

if symbols
    :Shivam
    println(:Shivam)

    d = Dict(:pi => 3.14, :e => 2.718)
    println(d[:pi])
end

if julia_struct
    #Immutable
    struct Customer
        name::String
        balance::Float32
        id::Int
    end

    bob = Customer("Bob Smith", 10.3, 23)
    println(bob.name, bob.balance, bob.id)
    #Immutable
    mutable struct MutCustomer
        name::String
        balance::Float32
        id::Int
    end
    bob = MutCustomer("Bob Smith", 10.3, 23)
    bob.id = 3
    println(bob)
end

if abstract_types
    abstract type Animal end

    struct Dog <: Animal
        name::String
        bark::String
    end

    struct Cat <: Animal
        name::String
        meow::String
    end

    bowser = Dog("Bowser", "Ruff")
    muffin = Cat("Muffin", "Meow")

    function makeSound(animal::Dog)
        println("$(animal.name) says $(animal.bark)")
    end
    function makeSound(animal::Cat)
        println("$(animal.name) says $(animal.meow)")
    end

    makeSound(bowser)
    makeSound(muffin)
end

if files
    open("test.txt", "w") do file
        write(file, "Here is some test text")
    end

    open("test.txt") do file
        data = read(file, String)
        println(data)
    end

    open("test.txt") do file
        for line in eachline(file)
            println(line)
        end
    end
end

