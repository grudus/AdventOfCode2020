package com.grudus.adventofcode;

import com.google.common.graph.Traverser;
import io.vavr.collection.List;
import io.vavr.collection.Map;

import java.util.Objects;
import java.util.regex.Pattern;
import java.util.stream.StreamSupport;

import static java.lang.Integer.parseInt;

public class Day07 extends Day<Integer> {

    record BagWithCount(String color, int count) {
        public boolean equals(Object o) {
            return Objects.equals(color, ((BagWithCount) o).color);
        }

        public int hashCode() {
            return Objects.hash(color);
        }
    }

    record Node<T>(T value, List<Node<T>> children) {
    }

    @SuppressWarnings("UnstableApiUsage")
    @Override
    public Integer firstStar(List<String> input) {
        List<Node<BagWithCount>> forest = createForest(input);

        return forest.map(tree ->
                StreamSupport.stream(Traverser.<Node<BagWithCount>>forGraph(node -> node.children)
                        .breadthFirst(tree)
                        .spliterator(), false)
                        .filter(x -> x.value.color.equals("shiny gold"))
                        .count())
                .sum().intValue() - 1;
    }

    @Override
    public Integer secondStar(List<String> input) {
        List<Node<BagWithCount>> forest = createForest(input);
        Node<BagWithCount> root = forest.find(tree -> tree.value.color.equals("shiny gold")).get();
        return calculateSize(root) - 1;
    }

    private Integer calculateSize(Node<BagWithCount> root) {
        if (root.children().isEmpty()) {
            return 1;
        }
        int numOfChildBags = root.children().map(child -> child.value().count * calculateSize(child)).sum().intValue();
        return 1 + numOfChildBags;
    }

    private List<Node<BagWithCount>> createForest(List<String> input) {
        Pattern pattern = Pattern.compile("(\\d+) (.*)");
        Map<BagWithCount, List<BagWithCount>> bagRules = input
                .map(line -> line.replaceAll("bags?|\\.", ""))
                .map(line -> line.split("contain"))
                .toMap(
                        parts -> new BagWithCount(parts[0].trim(), 1),
                        parts -> List.of(parts[1].split(","))
                                .map(String::trim)
                                .map(numAndColor -> Utils.findRegexGroups(pattern, numAndColor))
                                .map(numAndColor -> numAndColor.isEmpty() // no other
                                        ? null
                                        : new BagWithCount(numAndColor.get(1), parseInt(numAndColor.get(0))))
                );

        return bagRules.keySet().map(key -> createTreeNode(bagRules, key)).toList();
    }

    private <T> Node<T> createTreeNode(Map<T, List<T>> bagRules, T current) {
        List<T> children = bagRules.getOrElse(current, List.empty());
        List<Node<T>> map = children
                .filter(Objects::nonNull)
                .map(a -> createTreeNode(bagRules, a));
        return new Node<>(current, map);
    }
}
