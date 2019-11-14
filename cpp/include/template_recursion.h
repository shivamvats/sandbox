#ifndef SANDBOX_TEMPLATE_RECURSION_H
#define SANDBOX_TEMPLATE_RECURSION_H

template<unsigned...>
struct Sum;

template<unsigned size>
struct Sum<size> {
    enum {value = size};
};
template<unsigned size, unsigned...sizes>
struct Sum<size, sizes...> {
    enum { value = size + Sum<sizes...>::value };
};

static_assert( Sum<1, 2, 3>::value == 6, "" );

template <typename T>
T add(T arg)
{
    return arg;
}

template <typename T, typename... Ts>
T add(T first, Ts... args)
{
    return first + add(args...);
}

#endif
