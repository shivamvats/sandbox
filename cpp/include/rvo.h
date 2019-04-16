#ifndef RVO_H
#define RVO_H

/**
 * Tests Return Value Optimization (RVO).
 */

class MyClass {
    public:
    MyClass();
    explicit MyClass( int );
    MyClass( const MyClass& );

    int m_val;
};

#endif /* ifndef RVO_H */
