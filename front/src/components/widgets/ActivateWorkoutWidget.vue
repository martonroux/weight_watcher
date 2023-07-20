<script setup>
import Button from "@/components/elements/Button.vue";
import PopUpWindow from "@/components/elements/PopUpWindow.vue";
</script>

<template>
  <div class="activate-workout-widget">
    <h2>Activate workout</h2>
    <Button :text="'>'" style="padding: 5px 10px 5px 10px; border-radius: var(--widget-border-radius)" @clicked="togglePopup"/>
    <div class="activate-workout-popup" v-if="activePopup">
      <div class="activate-workout-title">
        <h2>Activate workout</h2>
      </div>
      <ol>
        <li v-for="(wrkt, index) in allWrkts" :key="index">
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
            <h2>{{ wrkt["name"] }}</h2>
          </div>
        </li>
      </ol>
      <div class="align-center" style="align-self: center; margin-top: 20px;">
        <Button :img-url="'close.png'" style="padding: 3px 8px 3px 8px; font-size: 24px; margin-right: 10px" @clicked="closeWindow(true)"/>
        <Button :img-url="'check_black.png'" style="padding: 5px 8px 5px 8px;" @clicked="closeWindow(false)"/>
      </div>
    </div>
    <PopUpWindow :open="warningPopUpOpen" :only-ok="true" ref="popup" @closed="closeWarningPopUp" style="margin: 10px">
      <p>You need to select a workout before going forward.</p>
    </PopUpWindow>
  </div>
</template>

<script>
import {putNewActiveWorkout} from "@/js_components/put_requests";

export default {
  data () {
    return {
      activePopup: false,
      selected: -1,
      warningPopUpOpen: false
    }
  },
  props: ["allWrkts"],
  methods: {
    togglePopup() {
      this.activePopup = true;
      this.selected = -1;
    },
    changeSelected(index) {
      this.selected = index;
    },
    closeWindow(escape) {
      if (this.selected === -1 && escape === false) {
        this.warningPopUpOpen = true;
      } else {
        this.activePopup = false;
        if (escape === false) {
          putNewActiveWorkout(this.allWrkts[this.selected]);
          this.$router.push("/");
        }
      }
    },
    closeWarningPopUp() {
      this.warningPopUpOpen = false;
    }
  }
}
</script>

<style scoped>

.activate-workout-widget {
  width: auto;
  height: auto;
  margin: var(--widget-margin);
  padding: var(--widget-padding);
  background-color: var(--widget-color);
  border-radius: var(--widget-border-radius);
  box-shadow: var(--widget-box-shadow);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

.activate-workout-popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10000;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
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

@media (min-width: 500px) {
  .activate-workout-popup ol {
    width: fit-content;
  }

  .activate-workout-popup {
    align-items: center;
  }
}

@media (max-width: 500px) {
  .activate-workout-title {
    display: flex;
    justify-content: center;
    align-items: center;
  }
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