<template>
  <div class="good-form">
    <el-page-header @back="$router.back()" content="新增商品"></el-page-header>
    <el-form
      style="width: 600px; margin-top: 20px"
      :model="ruleForm"
      :rules="rules"
      ref="ruleForm"
      label-width="100px"
      class="demo-ruleForm"
    >
      <!-- 商品名称 -->
      <!-- prop="name" 前端进行数据校验 -->
      <el-form-item label="商品名称" prop="name">
        <el-input v-model="ruleForm.name"></el-input>
      </el-form-item>

      <!-- 商品描述 -->
      <el-form-item label="商品描述" prop="desc">
        <el-input type="texterea" rows="3" v-model="ruleForm.desc"></el-input>
      </el-form-item>

      <!-- 商品分类 -->
      <el-form-item label="商品分类" prop="cate">
        <CateSelect></CateSelect>
      </el-form-item>

      <!-- 商品价格 -->
      <el-form-item label="商品价格" prop="price">
        <el-input-number
          :min="0"
          :step="0.1"
          :precision="2"
          v-model="ruleForm.price"
        ></el-input-number>
      </el-form-item>

      <!-- 是否热销 -->
      <el-form-item label="是否热销" prop="hot">
        <el-switch v-model="ruleForm.hot"></el-switch>
      </el-form-item>

      <!-- 商品图片 -->
      <el-form-item label="商品图片" prop="type">
        <!-- action 就是图片上传的接口 -->
        <ImgUpload></ImgUpload>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')"
          >提交</el-button
        >
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import CateSelect from "./components/CateSelect.vue";
import ImgUpload from "./components/ImgUpload.vue";

export default {
  name: "goodForm",
  props: [],
  components: {
    CateSelect,
    ImgUpload,
  },
  data() {
    return {
      ruleForm: {
        name: "",
        desc: "",
        cate: "",
        price: 0,
        hot: true,
        img: "",
      },
      rules: {
        // 对name这个字段进行校验
        name: [
          { required: true, message: "请输入商品名称", trigger: "blur" },
          {
            pattern: /[\u4e00-\u9fa5]{4,8}/,
            message: "商品名称要求4~8个中文汉字",
            trigger: "blur",
          },
        ],
        desc: [
          { required: true, message: "请填写商品介绍", trigger: "blur" },
          {
            min: 20,
            max: 30,
            message: "商品名称要求20~30个字符",
            trigger: "blur",
          },
        ],
        cate: [
          { required: true, message: "请选择商品品类", trigger: "blur" },
        ],
        price: [
          { required: true, message: "请填写商品价格", trigger: "change" },
        ],
        img: [{ required: true, message: "请上传商品图片", trigger: "change" }],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("submit!");
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
  },
};
</script>

<style>
.good-form {
  box-sizing: border-box;
  padding: 20px;
}
</style>