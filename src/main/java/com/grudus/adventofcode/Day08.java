package com.grudus.adventofcode;

import io.vavr.Function2;
import io.vavr.Tuple2;
import io.vavr.collection.List;
import io.vavr.collection.Map;
import io.vavr.collection.Stream;

import java.util.HashSet;
import java.util.Set;

public class Day08 extends Day<Integer> {
    record State(Integer lineNumber, Integer value) {}

    record Instruction(InstructionType type, Integer value) {
        public State execute(State state) {
            return type.action.apply(state, value);
        }
        public boolean canToggle() {
            return type != InstructionType.ACC;
        }
        public Instruction toggle() {
            return type == InstructionType.JMP
                    ? new Instruction(InstructionType.NOP, value)
                    : new Instruction(InstructionType.JMP, value);
        }
    }

    enum InstructionType {
        ACC((state, val) -> new State(state.lineNumber + 1, state.value + val)),
        JMP((state, val) -> new State(state.lineNumber + val, state.value)),
        NOP((state, val) -> new State(state.lineNumber + 1, state.value));
        public final Function2<State, Integer, State> action;
        InstructionType(Function2<State, Integer, State> action) {
            this.action = action;
        }
    }

    @Override
    public Integer firstStar(List<String> input) {
        Map<Integer, Instruction> instructions = input
                .map(this::parseInstruction)
                .zipWithIndex()
                .toMap(Tuple2::_2, Tuple2::_1);

        return runInstructions(instructions).value;
    }

    @Override
    public Integer secondStar(List<String> input) {
        Map<Integer, Instruction> instructions = input
                .map(this::parseInstruction)
                .zipWithIndex()
                .toMap(Tuple2::_2, Tuple2::_1);

        return Stream.range(0, instructions.size())
                .filter(i -> instructions.get(i).get().canToggle())
                .map(i -> instructions.put(i, instructions.get(i).get().toggle()))
                .map(this::runInstructions)
                .find(state -> state.lineNumber >= instructions.size())
                .get().value;
    }

    private State runInstructions(Map<Integer, Instruction> instructions) {
        Set<Integer> executedLines = new HashSet<>();

        return Stream.iterate(new State(0, 0),
                state -> instructions.getOrElse(state.lineNumber, new Instruction(InstructionType.JMP, 1)).execute(state))
                .takeWhile(state -> state.lineNumber <= instructions.size())
                .takeWhile(state -> !executedLines.contains(state.lineNumber))
                .peek(state -> executedLines.add(state.lineNumber))
                .last();
    }

    private Instruction parseInstruction(String s) {
        return new Instruction(
                InstructionType.valueOf(s.substring(0, 3).toUpperCase()),
                Integer.parseInt(s.substring(4))
        );
    }
}
