---
redirect_from:
  - /ocaml/cardstuff/2016/10/14/ocaml-algebraic-data-types
layout: post
title:  "OCaml algebraic data types and pattern matching"
date:   2016-10-14 18:30:00 -0400
categories: ocaml cardstuff
images: 🎰
---

I wrote a royal flush simulator in OCaml just to not forget the language.

[Here it is](https://github.com/jakekara/ocaml-cardstuff)

OCaml is cool. I took a class, Abstraction and Design in Computation, that
used OCaml exclusively. It was a good language for that class because we
began with functional programming, including using modules and functors,
and then moved to object oriented programming. It handles both paradigms
well.

A fellow programmer who doesn't write functional code asked why I liked
OCaml after taking this class, and I told him about algebraic data
types. The best example I could think of was expressing a deck of cards in
code, which is certainly possible in any programming paradigm and language,
but I think much more pleasant in OCaml.

Here's an algebraic data type I defined to represet card faces (in cards.ml):

{% highlight ocaml %}
type face_value =
  | Ace | Two | Three | Four | Five
  | Six | Seven | Eight | Nine | Ten
  | Jack | Queen | King
{% endhighlight %}

I did the same thing to define a type for suits...

{% highlight ocaml %}
(* Type for card suits*)
type suit =
  | Diamonds | Clubs | Hearts | Spades
{% endhighlight %}

... and then defined a card as a suit, face tuple:

{% highlight ocaml %}
(* Type for cards *)
type card = suit * face_value
{% endhighlight %}

Now I could use variables to represent each face value and assign a numeric
value, but that has a few drawbacks.

First of all, because face_value is a type now, OCaml will handle
enforcement anywhere you specificy you want a face_value. You don't have to
just use an int and then check every time that it's within the specified
range.

Second, it's easier to read.

Third, with OCaml's pattern matching, I now use these types to write
relatively readable, and short, code to test for a royal flush:

{% highlight ocaml %}

(* Test whether hand is a royal flush *)
let royal_flush (hand : card list) : bool =
  let suit, _ = List.nth hand 0 in
  hands_match hand
    ([(suit, Ace);(suit, King);
    (suit, Queen);(suit, Jack);(suit, Ten)])
{% endhighlight %}

This method takes a hand (a list of items of type card) and then tests if
it matches the "pattern" for a royal flush. A royal flush contains an Ace,
King, Queen, Jack and Ten, all of the same suit. I take the "suit" of the
first card, and then test whether the pattern holds. Notice that "suit" is
a variable.

I believe the above code is much more elegant and readable than could
otherwise be written without pattern matching and algebraic data types.

I don't get to use OCaml in my daily work, and I miss it.