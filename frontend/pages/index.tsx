import {
  NextPageContext,
  NextComponentType,
} from 'next';

import { compose } from 'recompose';
import { connect } from 'react-redux';

import Page from '../containers/page';
import { addTodo } from '../redux/actions';
import { Store } from '../redux/store';

interface IndexPageContext extends NextPageContext {
  store: Store;
}

const IndexPage: NextComponentType<IndexPageContext> = compose()(Page);

IndexPage.getInitialProps = ({ store, req }) => {
  const isServer: boolean = !!req;

  // we can add any custom data here
  const { todo } = store.getState();
  store.dispatch(addTodo(Object.assign(todo.item, {
    value: 'ELO!',
  })));

  return {
    isServer,
  };
}

export default connect()(IndexPage);