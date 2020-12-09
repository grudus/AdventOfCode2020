package com.grudus.adventofcode;

import io.vavr.collection.List;
import io.vavr.collection.Stream;

import static com.google.common.collect.Lists.cartesianProduct;
import static io.vavr.collection.List.ofAll;

public class Day09 extends Day<Long> {

    @Override
    public Long firstStar(List<String> input) {
        var preamble = 25;
        var parsedInput = input.map(Long::parseLong);
        return parsedInput
                .zipWithIndex()
                .drop(preamble)
                .find(xmasWithIndex -> {
                    var value = xmasWithIndex._1;
                    var prevNValues = parsedInput.subSequence(xmasWithIndex._2 - preamble, xmasWithIndex._2);
                    var prevCombinations = cartesianProduct(prevNValues.toJavaList(), prevNValues.toJavaList());
                    var prevSums = ofAll(prevCombinations).map(combinations -> ofAll(combinations).sum());
                    return !prevSums.contains(value);
                })
                .get()._1;
    }

    @Override
    public Long secondStar(List<String> input) {
        var parsedInput = input.map(Long::parseLong);
        var invalidValue = firstStar(input);

        return Stream.range(0, parsedInput.size())
                .flatMap(i -> Stream.range(i + 1, parsedInput.size())
                        .map(j -> parsedInput.subSequence(i, j)).toList())
                .find(sequence -> sequence.sum().equals(invalidValue))
                .map(sequence -> sequence.min().get() + sequence.max().get())
                .get();
    }
}
