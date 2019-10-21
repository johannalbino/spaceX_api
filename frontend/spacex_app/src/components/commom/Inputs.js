import React, { useState, useRef, useEffect } from 'react';
import TextField from '@material-ui/core/TextField';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import FormHelperText from '@material-ui/core/FormHelperText';
import MaskedInput from 'react-text-mask';

function TextMaskStateNumber(props) {
  const { inputRef, ...rest } = props;
  return (
    <MaskedInput
      {...rest}
      ref={ref => {
        inputRef(ref ? ref.inputElement : null);
      }}
      mask={() => [
        /\d/,
        /\d/,
        '.',
        /\d/,
        /\d/,
        /\d/,
        '.',
        /\d/,
        /\d/,
        /\d/,
        '/',
        /\d/,
        /\d/,
        /\d/,
        /\d/,
        '-',
        /\d/,
        /\d/
      ]}
      placeholderChar={'\u2000'}
      guide={false}
    />
  );
}

function TextMaskPhoneNumber(props) {
  const { inputRef, ...rest } = props;
  return (
    <MaskedInput
      {...rest}
      ref={ref => {
        inputRef(ref ? ref.inputElement : null);
      }}
      mask={() => [
        '(',
        /\d/,
        /\d/,
        ')',
        ' ',
        /\d/,
        /\d/,
        /\d/,
        /\d/,
        '-',
        /\d/,
        /\d/,
        /\d/,
        /\d/
      ]}
      placeholderChar={'\u2000'}
      guide={false}
    />
  );
}

function TextMaskCelPhoneNumber(props) {
  const { inputRef, ...rest } = props;
  return (
    <MaskedInput
      {...rest}
      ref={ref => {
        inputRef(ref ? ref.inputElement : null);
      }}
      mask={() => [
        '(',
        /\d/,
        /\d/,
        ')',
        ' ',
        /\d/,
        /\d/,
        /\d/,
        /\d/,
        /\d/,
        '-',
        /\d/,
        /\d/,
        /\d/,
        /\d/
      ]}
      placeholderChar={'\u2000'}
      guide={false}
    />
  );
}

export function Input({ type = 'text', mask, ...rest }) {
  return <TextField variant="outlined" type={type} {...rest} />;
}

export function StateNumberInput({ ...rest }) {
  return (
    <Input {...rest} InputProps={{ inputComponent: TextMaskStateNumber }} />
  );
}

export function PhoneNumberInput({ ...rest }) {
  return (
    <Input {...rest} InputProps={{ inputComponent: TextMaskPhoneNumber }} />
  );
}
export function CelPhoneNumberInput({ ...rest }) {
  return (
    <Input {...rest} InputProps={{ inputComponent: TextMaskCelPhoneNumber }} />
  );
}

export function SelectInput({
  name,
  label,
  options,
  className,
  error,
  helperText,
  ...rest
}) {
  const inputLabel = useRef(null);
  const [labelWidth, setLabelWidth] = useState(0);

  useEffect(() => {
    setLabelWidth(inputLabel.current.offsetWidth);
  }, []);

  return (
    <FormControl variant="outlined" className={className} error={error}>
      <InputLabel ref={inputLabel} htmlFor={name}>
        {label}
      </InputLabel>
      <Select
        {...rest}
        input={<OutlinedInput labelWidth={labelWidth} name={name} id={name} />}
      >
        {options &&
          options.map((option, index) => (
            <MenuItem key={index} value={option.value}>
              {option.text}
            </MenuItem>
          ))}
      </Select>
      {helperText && (
        <FormHelperText id="helper-text">{helperText}</FormHelperText>
      )}
    </FormControl>
  );
}
