<template>
  <div class="login">
    <input type="text" v-model="textInput" @keyup.enter="submit">
  </div>
</template>

<script>
export default {
  data () {
    return {
      textInput: '',
    };
  },
  methods: {
    submit() {
      console.log("Input:", this.textInput);
    }
  }
}
</script>

<style scoped>

</style>