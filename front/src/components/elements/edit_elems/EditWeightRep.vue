<script setup>
import Button from "@/components/elements/Button.vue";
</script>

<template>
  <div class="edit-weight-rep" @keyup.esc="closeWindow(true)">
    <div class="align-center" style="align-self: center">
      <div class="weight-rep-modif-display">
        <p>REPS</p>
        <p>WEIGHT</p>
      </div>
      <ol>
        <li v-for="(reps, index) in repData" :key="index">
          <div class="weight-rep-modif-display" style="margin-right: 10px">
            <input ref="editRepInput" class="edit-weight-rep-input" type="number" v-model="repData[index]" inputmode="decimal"/>
            <input ref="editWeightInput" class="edit-weight-rep-input" type="number" v-model="weightData[index]" inputmode="decimal"/>
          </div>
          <Button :img-url="'delete.png'" style="height: 35px; padding: 0 5px 0 5px; border-radius: var(--widget-border-radius); background-color: var(--major-color)" @clicked="openPopup(index)"/>
          <PopUpWindow :open="popUpOpen === index" ref="popup" @closed="closePopup">
            <p>Are you sure?</p>
            <p>Deleting is irreversible.</p>
          </PopUpWindow>
        </li>
        <li class="add-button">
          <Button :text="'+'" style="width: 100%; padding: 0; height: 35px; border-radius: var(--widget-border-radius);" @clicked="addNewLine"/>
        </li>
      </ol>
    </div>
    <div class="align-center" style="align-self: center;">
      <Button :img-url="'close.png'" style="padding: 3px 8px 3px 8px; font-size: 24px; margin-right: 10px" @clicked="closeWindow(true)"/>
      <Button :img-url="'check_black.png'" style="padding: 5px 8px 5px 8px;" @clicked="closeWindow(false)"/>
    </div>
  </div>
</template>

<script>
import PopUpWindow from "@/components/elements/PopUpWindow.vue";

export default {
  data () {
    return {
      popUpOpen: -1,
      repDataSave: {},
      weightDataSave: {}
    }
  },
  props: ['repData', 'weightData', 'index'],
  components: {
    PopUpWindow
  },
  watch: {
    weightData: {
      immediate: true,
      handler() {
        this.weightDataSave = JSON.parse(JSON.stringify(this.weightData));
      }
    },
    repData: {
      immediate: true,
      handler() {
        this.repDataSave = JSON.parse(JSON.stringify(this.repData));
      }
    }
  },
  methods: {
    closeWindow(escape) {
      if (escape === false) {
        this.$emit('close');
      } else {
        Object.assign(this.weightData, this.weightDataSave);
        Object.assign(this.repData, this.repDataSave);
        this.$emit('close');
      }
    },
    addNewLine() {
      this.weightData.push(0);
      this.repData.push(0);
    },
    openPopup(index) {
      this.popUpOpen = index;
    },
    closePopup(isOk) {
      if (isOk === true) {
        const index = this.popUpOpen;

        this.weightData.splice(index, 1);
        this.repData.splice(index, 1);
      }
      this.popUpOpen = -1;
    }
  }
}
</script>

<style scoped>

.edit-weight-rep {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 9999;
  backdrop-filter: blur(10px);
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.edit-weight-rep li {
  display: flex;
  flex-direction: row;
}

.edit-weight-rep-input {
  font-size: var(--body-font-size);
  color: var(--text-white);
  width: 70px;
  background-color: transparent;
  border: none;
  outline: none;
  padding: 0 2px 0 10px;
}

.weight-rep-modif-display {
  background-color: var(--backround-color);
  border-radius: var(--widget-border-radius);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 180px;
  height: 35px;
  margin-bottom: 10px;
}

.add-button {
  justify-content: center;
  margin-bottom: 40px;
}

@media(max-width: 240px) {
  .weight-rep-modif-display {
    width: 70vw;
  }
}

.weight-rep-modif-display p {
  margin: 7px;
}

img {
  height: var(--h2-font-size);
  width: var(--h2-font-size);
  padding: 0;
  margin: 0;
}

</style>