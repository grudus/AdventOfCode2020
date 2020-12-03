package com.grudus.adventofcode;


import io.vavr.collection.List;

public abstract class Day<T> {

    public abstract T firstStar(List<String> input);
    public abstract T secondStar(List<String> input);
}
