<template>
  <img :class="{'wrkt-image': !imgClicked, 'wrkt-image-active': imgClicked}"
        :src="imgPath" alt="edit" @click="wrktImageClicked">
</template>

<script>
export default {
  data () {
    return {
      imgPath: "./src/assets/icons/edit.png",
      imgClicked: false,
      isEditing: false,
    }
  },
  methods: {
    wrktImageClicked() {
      this.imgClicked = true;
      this.isEditing = !this.isEditing;

      if (this.isEditing === false) {
        this.imgPath = "./edit.png";
      } else {
        this.imgPath = "./check.png";
      }
      this.$emit('clicked');
    }
  }
}
</script>

<style scoped>

.wrkt-image {
  transition: scale 0.2s;
  cursor: pointer;
}

.wrkt-image:hover {
  scale: 96%;
}

.wrkt-image-active {
  scale: 90%;
}

</style>