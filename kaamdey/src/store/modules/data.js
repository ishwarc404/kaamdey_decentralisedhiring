
const state = {
  searchContent:null

};
const getters = {
  getsearchContent: (state) => state.searchContent,

};

const actions = {
  async updatesearchContent({ commit }, searchContent) {
    commit("setsearchContent", searchContent);
  },

};

const mutations = {
  setsearchContent: (state, searchContent) => (state.searchContent = searchContent),

};

export default {
  state: state,
  getters: getters,
  actions: actions,
  mutations: mutations,
};
