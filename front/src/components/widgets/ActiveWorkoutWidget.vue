<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="widget">
    <div class="row" style="display: flex; flex-direction: row; justify-content: space-between; align-items: center;">
      <h2 style="color: var(--accentuation-color);">{{ workout['name'] }}</h2>
      <div class="time">
        <div class="circle">
          <div>
            <span class="minutes"></span>
            <span class="hours"></span>
          </div>
        </div>
        <p>{{ time }}</p>
      </div>
    </div>
    <div class="active-exercise">
      <div class="row" style="display: flex; flex-direction: row; justify-content: flex-end; align-items: center;">
        <h2 style="font-size: var(--body-font-size); justify-self: flex-start; margin-right: auto;">{{ activeExercise }}</h2>
        <Button style="padding: 5px 6px 3px 7px" :img-url="'swap.png'"></Button>
        <Button style="padding: 5px 6px 3px 7px" :img-url="'forward-button.png'"></Button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      time: '',
      activeExercise: ''
    }
  },
  props: ['workout'],
  mounted() {
    this.updateTime();
  },
  watch: {
    'workout': {
      immediate: true,
      handler() {
        if (this.workout && this.workout['exercises'] && this.workout['exercises'].length > 0) {
          this.activeExercise = this.workout['exercises'][0]['name'];
        }
      }
    }
  },
  methods: {
    getCurrentTime() {
      const currentTime = Date.now();
      const diff = currentTime - (this.workout['start_date'] * 1000);
      const seconds = Math.floor(diff / 1000);
      const minutes = Math.floor(seconds / 60);
      const hours = Math.floor(minutes / 60);
      const days = Math.floor(hours / 24);

      let timestamp = '';
      if (days > 0) timestamp += `${days}j `;
      if (hours > 0) timestamp += `${hours % 24}h `;
      if (minutes > 0) timestamp += `${minutes % 60}min `;
      timestamp += `${seconds % 60}s`;

      this.time = timestamp;
    },
    updateTime() {
      this.getCurrentTime();
      setTimeout(() => this.updateTime(), 1000);
    }
  }
}
</script>

<style scoped>

.widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
  display: flex;
  flex-direction: column;
}

.time {
  display: flex;
  flex-direction: row;
  align-items: center;

  .circle {
    margin-right: 20px;
  }
}

.active-exercise {
  margin-top: 20px;

  .row :not(:last-child) {
    margin-right: 10px;
  }
}

.circle {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background-color: transparent;
  border: 2px solid var(--text-white);
  flex-shrink: 0;
}

.circle div {
  position: relative;
  top: 45%;
  left: -48%;
  display: flex;
  justify-content: flex-end;
  padding: 0;
}

.circle span {
  background: var(--text-white);
  height: 3px;
  border-radius: 5px;
  position: absolute;
  transition: width 0.3s;
  margin: 0;
}

.circle .minutes {
  transform-origin: 93% 50%;
  width: 42%;
  animation: rotate 10s linear infinite;
}

.circle .hours {
  transform-origin: 92% 50%;
  width: 32%;
  transform: translate(8%, 0%);
  animation: rotate 20s linear infinite;
}

</style>