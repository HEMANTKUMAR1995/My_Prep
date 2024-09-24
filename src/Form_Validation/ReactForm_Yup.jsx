import React from "react";
import { useForm } from "react-hook-form";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
//React Hook Form -> this is a schema based way of form validation this supports yup for schema creation
const schema = yup.object().shape({
  username: yup.string().required(" userName is required"),
  email: yup.string().email("invalid email").required("email is required"),
  password: yup
    .string()
    .min(8, "min 8 characters are required")
    .required("password is required"),
});
const ReactForm_Yup = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const onSubmit = (data) => {
    console.log(data);
  };
  return (
    <>
      <form onSubmit={handleSubmit(onSubmit)}>
        <>
          <label>userName</label>
          <input {...register("username")} />
          {errors.username && <p>{errors.username.message}</p>}
        </>
        <>
          <label>email</label>
          <input {...register("email")} />
          {errors.email && <p>{errors.email.message}</p>}
        </>
        <>
          <label>password</label>
          <input {...register("password")} />
          {errors.password && <p>{errors.password.message}</p>}
        </>
        <button type="submit">Submit</button>
      </form>
    </>
  );
};

export default ReactForm_Yup;
