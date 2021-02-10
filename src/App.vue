<template>
  <div id="app">
    <GameCardsStack
      :cards="visibleCards"
      @rightE="handlerightE"
      @leftE="handleleftE"
      @downE="handledownE"
      @upE="handleupE"
      @hideCard="removeCardFromDeck"
    />
  </div>
</template>

<script>
import GameCardsStack from "./components/GameCardsStack";
export default {
  name: "App",
  components: {
    GameCardsStack,
  },

  data() {
    return {
      visibleCards: [
        "Swipe any way",
        "The pupose of this test is to determine your eye power.",
        "To meet the purpose of this test you need to follow the specified instructions",
        "1. You will see an E shapped letter",
        "2. Upon seeing this E shaped object you need to determine the direction the open ended side of the letter is facing",
        "3. Slide the card to the direction of the open ended side",
        "For example you see M you have to slide the card downward",
        "Now give it a try, Which way do you slide the next card",
        "E",
        "Ǝ",
        "m",
        "ɯ",
      ],
    };
  },
  methods: {
    handlerightE() {
      console.log("swipe_rightE");
    },
    handleleftE() {
      console.log("swipe_leftE");
    },
    handledownE() {
      console.log("swipe_downE");
    },
    handleupE() {
      console.log("swipe_upE");
    },
    removeCardFromDeck() {
      this.visibleCards.shift();
    },
  },
};
</script>

<style lang="scss">
@import "./styles/mixins.scss";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
}
</style>
