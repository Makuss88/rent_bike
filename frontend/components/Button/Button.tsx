import React from 'react';
import Link from 'next/link';
import styled from 'styled-components'

import { Button as MuiButton, ButtonProps } from '@material-ui/core';

interface Props extends ButtonProps{
	children: React.ReactNode;
	isCircled: boolean;
	href: string;
}

const StyledButton = styled(React.forwardRef<HTMLButtonElement, Props>(({ children, isCircled, ...rest }, ref) => (
	<MuiButton children={children} {...rest} innerRef={ref} />))
)`
	border-radius: ${(props: Props) => props.isCircled ? '25px' : '10px'}!important;
`;


const Button = React.forwardRef<HTMLButtonElement, Props>((props, ref) => {
	const { href, isCircled, children } = props;
	if (href) {
		return (
			<Link href={href}>
				<StyledButton isCircled={isCircled} ref={ref} children={children} {...props} />
			</Link>
		)
	}
	return (
		<StyledButton isCircled={props.isCircled} ref={ref} >
			{props.children}
		</StyledButton>
	)
});

export default Button;