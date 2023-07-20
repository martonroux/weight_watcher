<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="switch-exercise">
    <h2>Next exercise</h2>
    <ol>
      <li v-for="(exercise, index) in exercises" :key="index">
        <div class="selector" @click="changeSelected(index)">
          <div class="check-box">
            <div>
                <span class="line-1" :style="{
                  'background-color': (selected === index) ? 'var(--text-white)' : 'transparent',
                  width: (selected === index) ? '40%' : 0,
                }"></span>
              <span class="line-2" :style="{
                  'background-color': (selected === index) ? 'var(--text-white)' : 'transparent',
                  width: (selected === index) ? '80%' : 0,
                }"></span>
            </div>
          </div>
          <h2>{{ exercise["name"] }}</h2>
        </div>
      </li>
    </ol>
    <div class="align-center" style="align-self: center; margin-top: 20px;">
      <Button :img-url="'check_black.png'" style="padding: 5px 8px 5px 8px;" @clicked="closeWindow"/>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: 0
    }
  },
  props: ['exercises'],
  emits: ['newExercise'],
  methods: {
    changeSelected(index) {
      this.selected = index;
    },
    closeWindow() {
      this.$emit('newExercise', this.exercises[this.selected]['name']);
    }
  }
}
</script>

<style scoped>

.switch-exercise {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10000;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.selector {
  width: auto;
  height: auto;
  margin: 10px;
  padding: 15px;
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.check-box {
  width: 30px;
  height: 30px;
  cursor: pointer;
  justify-self: flex-end;
  align-self: flex-end;
  border: 2px solid var(--text-white);
  border-radius: var(--widget-border-radius);
  margin-right: 30px;
}

.check-box div {
  position: relative;
  top: 40%;
  left: 5%;
}

.check-box span {
  background: var(--text-white);
  height: 6px;
  border-radius: 5px;
  position: absolute;
  transition: background-color 0.2s, width 0.3s;
}

.check-box .line-1 {
  width: 40%;
  transform: translate(8%, 55%) rotate(42deg);
}

.check-box .line-2 {
  width: 80%;
  transform: rotate(-48deg) translate(15%, 40%);
}

</style>