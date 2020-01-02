const mutation = {
  update_state(state, payload) {
    state.update_state = JSON.parse(JSON.stringify(payload));
  },
};

export default mutation;
