<template>
  <div class="parentTitle">
    <div class="childtitle Title">
      <div id="title_name">
        <h1>
          <span><strong class="username">{{ resume.name }}</strong></span>
        </h1>
      </div>
      <div id="title_description_job">
        <h4>
          <span><strong class="career-highlight">{{ resume.user_contact_details[0].user_work_title }}</strong></span>
        </h4>
      </div>
      <div class="row">
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-telephone"></i>
          <span><strong class="phone_number">{{ resume.user_contact_details[0].phone_number }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-envelope-at"></i>
          <span><strong class="email">{{ resume.email }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-linkedin"></i>
          <span><strong class="linkedIn">some linkedIn url</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-link-45deg"></i>
          <span><strong class="personal_website">{{ resume.user_contact_details[0].personal_website }}</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-github"></i>
          <span><strong>https://github.com/test</strong></span>
        </div>
        <div class="col-md-4 iconic-sectionTitle">
          <i class="bi bi-geo-alt-fill"></i>
          <span><strong class="address">{{ resume.user_contact_details[0].city }} , {{ resume.user_contact_details[0].country }}</strong></span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  const { resume } = defineProps(['resume'])
</script>

<style scoped></style>
