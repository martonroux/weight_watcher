<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="change-order"
       @keyup.enter="closeWindow"
       @keyup.esc="closeWindow"
       @mouseup="stopTracking"
       @mousemove="updatePosition"
       @touchmove="updatePosition"
       @touchend="stopTracking">
    <ol id="order-list">
      <li v-for="(exercise, index) in exerciseList" :key="index">
        <div class="change-order-content"
             @mousemove="updatePosition"
             @touchmove="updatePosition"
             @mouseup="stopTracking"
             @touchend="stopTracking"
             :style="{
               position: 'relative',
               top: (indexModif === index) ? (posY - mouseInitY) + 'px' : '0',
               left: (indexModif === index) ? (posX - mouseInitX) + 'px' : '0',
               'z-index': (indexModif === index) ? '10001' : '10000'}">
          <p style="user-select: none;">{{ exercise["name"] }}</p>
          <div class="menu-btn" id="menu-btn"
               @touchstart="event => startTracking(event, index)"
               @mousedown="event => startTracking(event, index)"
          :style="{cursor: (indexModif !== index) ? 'grab' : 'grabbing'}">
            <div>
              <span class="line-1"></span>
              <span class="line-2"></span>
              <span class="line-3"></span>
            </div>
          </div>
        </div>
      </li>
    </ol>
    <div class="align-center" style="align-self: center;">
      <Button :img-url="'check_black.png'" style="padding: 3px 8px 3px 8px; font-size: 24px; margin-right: 10px" @clicked="closeWindow"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      input: '',
      posX: -1,
      posY: -1,
      mouseInitX: -1,
      mouseInitY: -1,
      indexModif: -1,
      exerciseList: []
    }
  },
  props: ['workoutData'],
  emits: ['close'],
  watch: {
    'workoutData': {
      immediate: true,
      handler() {
        this.exerciseList = this.workoutData["exercises"];
      }
    },
  },
  methods: {
    closeWindow() {
      this.$emit('close');
    },
    updatePosition(event) {
      if (this.indexModif === -1)
        return;
      const isTouch = event.type === "touchmove";

      const clientX = isTouch ? event.touches[0].clientX : event.clientX;
      const clientY = isTouch ? event.touches[0].clientY : event.clientY;

      this.posX = clientX;
      this.posY = clientY;
      this.testOrderChanged(event);
    },
    startTracking(event, index) {
      if (this.indexModif === -1)
        this.indexModif = index;
      const isTouch = event.type === "touchmove";

      const clientX = isTouch ? event.touches[0].clientX : event.clientX;
      const clientY = isTouch ? event.touches[0].clientY : event.clientY;

      this.mouseInitX = clientX;
      this.mouseInitY = clientY;
      this.updatePosition(event);
    },
    stopTracking() {
      this.indexModif = -1;
    },
    restartTracking(event) {
      const isTouch = event.type === "touchmove";

      this.mouseInitY = isTouch ? event.touches[0].clientY : event.clientY;
      this.updatePosition(event);
    },
    testOrderChanged(event) {
      const liElement = document.getElementById("order-list").getElementsByTagName("li");
      const elem = liElement[this.indexModif];
      const elemY = elem.offsetTop + (this.posY - this.mouseInitY);
      let otherY = 0;

      for (let i = 0; i < liElement.length; i++) {
        if (i === this.indexModif)
          continue;
        otherY = liElement[i].offsetTop;

        if (i < this.indexModif) {
          if (elemY < otherY) {
            this.exerciseList[this.indexModif] = this.exerciseList.splice(i, 1, this.exerciseList[this.indexModif])[0];
            this.indexModif = i;
            this.restartTracking(event);
            return;
          }
        } else {
          if (elemY > otherY) {
            this.exerciseList[i] = this.exerciseList.splice(this.indexModif, 1, this.exerciseList[i])[0];
            this.indexModif = i;
            this.restartTracking(event);
            return;
          }
        }
      }
    }
  }
}
</script>

<style scoped>

.change-order {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.change-order-content {
  background-color: var(--widget-color);
  padding: 20px;
  border-radius: var(--widget-border-radius);
  position: absolute;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 300px;
}

@media (max-width: 400px) {
  .change-order-content {
    width: 75vw;
  }
}

.change-order *:not(:last-child) {
  margin-bottom: 10px;
}

.change-order *:not(:last-child) {
  margin-right: 2vw;
}

.menu-btn {
  width: 40px;
  height: 40px;
}

.menu-btn div {
  width: 60%;
  height: 60%;
  position: relative;
  top: 18%;
  left: 20%;
}

.menu-btn span {
  background: var(--text-white);
  width: 100%;
  height: 3px;
  border-radius: 5px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: transform 0.5s, width 0.5s;
}

.menu-btn .line-1 {
  transform: translate(-50%, -300%);
}

.menu-btn .line-3 {
  transform: translate(-50%, 200%);
}

</style>