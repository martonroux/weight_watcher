<template>
  <button :class="{'btn': !btnClicked, 'btn-active': btnClicked}" @click="handleClick">
    <span class="conditionnal" v-if="text">
      {{ text }}
    </span>
    <img :src="imgUrl" alt="check" v-if="imgUrl">
  </button>
</template>

<script>
export default {
  data () {
    return {
      btnClicked: false,
    }
  },
  props: ['text', 'imgUrl'],
  methods: {
    handleClick() {
      this.btnClicked = true;

      this.$emit('clicked');
      setTimeout(() => {
        this.btnClicked = false;
      }, 200);
    }
  }
}
</script>

<style scoped>

img {
  height: var(--body-font-size);
  width: var(--body-font-size);
}

.btn:hover {
  scale: 96%;
}

.btn-active {
  scale: 90%;
}

</style>