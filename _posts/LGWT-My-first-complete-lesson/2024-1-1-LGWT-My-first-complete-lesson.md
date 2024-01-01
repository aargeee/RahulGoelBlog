---
title: LGWT | My first complete lesson
date: 2024-1-1 5:40:5 -19800
tags: [2024, Go]
description: because satisfaction of completion
---

## What happened?

I stumbled upon this book and thought to myself, let's make a deal I am going to finish this book no matter what and I am going to finish it all the way through. And I had a deadline. 2023. I had a little more than 2 months to finish the book which should be more than enough theoritically. But I just had to make sure I don't give up midway. 
This will be a compilation of all the things I learnt and all the things I'm going to likely forget. So instead of working my way to the actual book, I want to get to the crux fast.

{% include Contents.md %}

## [Hello World](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/hello-world)

Let's start with the ceremony. 
* `fmt` package allows us to use a bunch of functions like `Print_()`, `Sprint_()` and `Fprint_()`. These come to use all the time. 
* We are met with our first iteration of TDD. Write failing tests -> Pass the test though the easy path -> Refactor!
* This is the smallest piece of example to highlight the TDD process. 
```Go
// Write failing test
// hello_test.go
package main
import "testing"
func TestHello(t *testing.T) {
	got := Hello()
	want := "Hello, world"
	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}
```
```Go
// Passing test through easy path
// hello.go
package main
import "fmt"
func Hello() string {
	return "Hello, world"
}
func main() {
	fmt.Println(Hello())
}
```
```Go
// Refactor
package main
import "fmt"
const GreetMessage = "Hello, world"
func Hello() string {
	return GreetMessage
}
func main() {
	fmt.Println(Hello())
}
```

## [Integers](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/integers)
* This was just to show that we can do maths in Go
* To install godoc use this `go install golang.org/x/tools/cmd/godoc@latest`
* Writing Examples for godoc 
```Go
// adder_test.go
func ExampleAdd() {
	sum := Add(1, 5)
	fmt.Println(sum)
	// Output: 6
}
```
```Go
// This is the overview
package numbergame
// Takes 2 integer numbers and returns the sum of them
func Adder(num1, num2 int) int {
	return num1 + num2
}
```
* The `// Output: 6` is required to be formatted as the output of the example. And the name `ExampleXXX()` is equally important to be registered as an example to show in the godoc. 
* Comment above the package is interpreted as Overview of package
* Comment above each function is the description of each function.
* Allows better documentation. I promise I will make my code documentation proof whenever I write anything.

## [Iteration](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals)
* This chapter taught me benchmarking. 
```Go
func BenchmarkRepeat(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Repeat("a")
	}
}
```
* To run this benchmark `go test -bench=.` 
* When the benchmark code is executed, it runs b.N times and measures how long it takes.
```bash
goos: linux
goarch: amd64
pkg: GoSayHello/03_Iteration
cpu: AMD EPYC 7763 64-Core Processor                
BenchmarkLoopy-2          257878              5591 ns/op
PASS
ok      GoSayHello/03_Iteration 2.410s
```
* Our function gives a performance of 5591 ns/op and it ran the function 257878 times.
* Another example from the book from the Concurrency chapter.
```Go
func BenchmarkCheckWebsites(b *testing.B) {
	urls := make([]string, 100)
	for i := 0; i < len(urls); i++ {
		urls[i] = "a url"
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		CheckWebsites(slowStubWebsiteChecker, urls)
	}
}
```
* We can use `b.ResetTimer()` to start counting from that instant. More in [Concurrency](#concurrency) Chapter.


## [Arrays and Slices](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/arrays-and-slices)
* There are two ways to declare an array in Go
    * [N]type{value1, value2, ..., valueN} e.g. numbers := [5]int{1, 2, 3, 4, 5}
    * [...]type{value1, value2, ..., valueN} e.g. numbers := [...]int{1, 2, 3, 4, 5}


