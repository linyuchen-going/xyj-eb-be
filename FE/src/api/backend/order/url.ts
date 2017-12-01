import parrentPath from '../url'


const orderPath = `${parrentPath}/order`;

export default orderPath;

export const apiUrlOrders = (page: number)=>`${orderPath}?p=${page}`;
