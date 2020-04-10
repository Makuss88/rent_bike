///REDUX CONFGURATION https://dev.to/saltyshiomix/learn-the-redux-architecture-by-creating-the-minimal-todo-app-on-top-of-next-js-5bpj
import { createSelector } from 'reselect';

export const selectState = () => state => state.todo;

export const selectTodoItem = () =>
  createSelector(
    selectState(),
    todo => todo.item,
  );

export const selectTodoData = () =>
  createSelector(
    selectState(),
    todo => todo.data,
  );